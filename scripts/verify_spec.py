"""Independent numerical audit of docs/MECHANICS.md at commit 45a9dbd8.

Run with Python 3.10+; no third-party packages. This checks planning math,
not a Three.js application, solid clearances, or the reference video.
"""
from __future__ import annotations

import json
import math

SPEC_COMMIT = "45a9dbd8ca2991ad6f17bba558fd147cfc5d6348"
R, L, BORE, STROKE, CR = 0.045, 0.150, 0.100, 0.090, 10.0
ALPHA0 = (-45.0, -135.0, 45.0, 135.0)
ORDER = (1, 8, 4, 3, 6, 5, 7, 2)
FIRE = {c: index * 90.0 for index, c in enumerate(ORDER)}
TOL = 1e-12
Vec3 = tuple[float, float, float]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def rotate_z(point: Vec3, degrees: float) -> Vec3:
    a = math.radians(degrees)
    x, y, z = point
    return (x * math.cos(a) - y * math.sin(a),
            x * math.sin(a) + y * math.cos(a), z)


def pose(cylinder: int, theta: float) -> tuple[Vec3, Vec3, float, float]:
    if cylinder not in FIRE or not math.isfinite(theta):
        raise ValueError("Known cylinder and finite phase required")
    journal = (cylinder - 1) // 2
    beta = math.radians(-45.0 if cylinder % 2 else 45.0)
    alpha = math.radians(ALPHA0[journal] - theta)
    # Axial offsets are arbitrary audit fixtures, NOT a finalized rod package.
    z = journal * 0.112 + (-0.010 if cylinder % 2 else 0.010)
    p = (R * math.sin(alpha), R * math.cos(alpha), z)
    ux, uy = math.sin(beta), math.cos(beta)
    q = p[0] * ux + p[1] * uy
    s = q + math.sqrt(L * L - R * R + q * q)
    w = (s * ux, s * uy, z)
    x_projected = R + L - s
    psi = math.radians((theta - FIRE[cylinder]) % 360.0)
    x_analytic = R * (1 - math.cos(psi)) + L - math.sqrt(
        L * L - R * R * math.sin(psi) ** 2)
    return p, w, x_projected, x_analytic


def events(old: float, new: float) -> list[tuple[float, int]]:
    if not (math.isfinite(old) and math.isfinite(new)) or new < old:
        raise ValueError("Finite, nondecreasing interval required; seeks emit no events")
    result = []
    for cylinder, fire in FIRE.items():
        first = math.floor((old - fire) / 720.0) + 1
        last = math.floor((new - fire) / 720.0)
        result.extend((fire + 720.0 * k, cylinder) for k in range(first, last + 1))
    return sorted(result)


def main() -> None:
    errors = dict.fromkeys(("rod_length_m", "formula_agreement_m", "render_matrix_m",
                           "pose_periodicity_m", "bank_alignment_m", "cam_matrix_m"), 0.0)
    phases = [k / 4.0 for k in range(2881)]
    extra_phases = [-1440.25, -720.0, -360.25, -0.25, 720.25, 1440.25]
    for cylinder in range(1, 9):
        journal = (cylinder - 1) // 2
        beta = -45.0 if cylinder % 2 else 45.0
        require((ALPHA0[journal] - FIRE[cylinder] - beta) % 360.0 == 0.0,
                f"Firing phase not at TDC: {cylinder}")
        for theta in phases + extra_phases:
            p, w, x, analytic = pose(cylinder, theta)
            require(-TOL <= x <= STROKE + TOL, "Travel out of range")
            require(p[2] == w[2], "Rod is not planar")
            errors["rod_length_m"] = max(errors["rod_length_m"], abs(math.dist(p, w) - L))
            errors["formula_agreement_m"] = max(errors["formula_agreement_m"], abs(x - analytic))
            errors["pose_periodicity_m"] = max(errors["pose_periodicity_m"],
                                                math.dist(w, pose(cylinder, theta + 360)[1]))
            authored = pose(cylinder, 0.0)[0]
            errors["render_matrix_m"] = max(errors["render_matrix_m"],
                                             math.dist(rotate_z(authored, theta), p))
            unit = rotate_z((0.0, 1.0, 0.0), -beta)
            errors["bank_alignment_m"] = max(errors["bank_alignment_m"],
                                              abs(w[0] * unit[1] - w[1] * unit[0]))
            # Positive Euler Theta/2 equals alpha0 - Theta/2 in the stated convention.
            cam_alpha = math.radians(ALPHA0[journal] - theta / 2)
            cam_expected = (R * math.sin(cam_alpha), R * math.cos(cam_alpha), authored[2])
            errors["cam_matrix_m"] = max(errors["cam_matrix_m"],
                                          math.dist(rotate_z(authored, theta / 2), cam_expected))
        require(abs(pose(cylinder, FIRE[cylinder])[2]) < TOL, "TDC error")
        require(abs(pose(cylinder, FIRE[cylinder] + 180)[2] - STROKE) < TOL, "BDC error")

    for key, error in errors.items():
        require(error < TOL, f"{key}: {error}")
    for odd in (1, 3, 5, 7):
        for theta in phases:
            a, b = pose(odd, theta)[0], pose(odd + 1, theta)[0]
            require(math.dist(a[:2], b[:2]) < TOL, "Shared journal radial mismatch")
            require(abs((b[2] - a[2]) - 0.020) < TOL, "Fixture rod-plane separation error")

    require([c for _, c in events(-1, 719)] == list(ORDER), "Firing order mismatch")
    require(len(events(0, 720)) == 8, "Incorrect complete-cycle event count")
    require(events(719, 721) == [(720.0, 1)], "Wraparound error")
    require(not events(720, 720), "Duplicate stationary event")
    for hz in (30, 60, 120):
        boundaries = [90.0 * k / hz for k in range(8 * hz + 1)]
        partitioned = [e for a, b in zip(boundaries, boundaries[1:]) for e in events(a, b)]
        require(partitioned == events(0, 720), "Partition-dependent firing events")

    swept = math.pi * BORE ** 2 / 4 * STROKE
    clearance = swept / (CR - 1)
    require(abs((swept + clearance) / clearance - CR) < TOL, "Volume ratio mismatch")
    print(json.dumps({
        "status": "PASS: planning equations only",
        "specification_commit": SPEC_COMMIT,
        "regular_pose_samples": len(phases) * 8,
        "additional_wrapped_pose_samples": len(extra_phases) * 8,
        "maximum_errors": errors,
        "tolerance_m": TOL,
        "displacement_liters": swept * 8 * 1000,
        "firing_order": ORDER,
        "crank_euler_sign": "positive Theta",
        "cam_euler_sign": "positive Theta/2",
        "shared_journal_checks": "PASS with explicitly arbitrary axial fixtures",
        "event_boundary_and_partition_checks": "PASS",
        "not_validated": ["application code", "actual renderer", "collision envelopes",
                          "valvetrain contact", "thermodynamic accuracy", "video fidelity",
                          "browser interactions", "accessibility", "performance", "deployment"]
    }, indent=2))


if __name__ == "__main__":
    main()
