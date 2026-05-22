#!/usr/bin/env python3
"""Verify object parsing for a spec directory.

Usage:
    python3 verify_objects.py [spec_dir]

Default spec_dir is 'spec/' relative to cwd.
Exits 0 if domain objects found, 1 if none found or errors.

NOTE: Must be run with a Python environment that has spec_parser_lib installed.
Example:
    cd /path/to/spec-parser-lib && poetry run python /path/to/this/script.py /path/to/repo/spec/
"""

import sys
from pathlib import Path

try:
    from spec_parser_lib.parser import parse_spec_directory
except ImportError:
    print(
        "ERROR: spec_parser_lib not installed. Install from agent-ix/spec-parser-lib."
    )
    sys.exit(1)


def main() -> int:
    spec_dir = sys.argv[1] if len(sys.argv) > 1 else "spec/"

    spec_path = Path(spec_dir)
    if not spec_path.is_dir():
        print(f"ERROR: '{spec_dir}' is not a directory")
        return 1

    artifacts = parse_spec_directory(spec_path)

    # Filter domain objects
    domain_artifacts = [
        a for a in artifacts if a.spec_metadata and a.spec_metadata.get("domain")
    ]
    domain_count = len(domain_artifacts)

    print(f"=== Domain Object Verification: {spec_dir} ===")
    print(f"Total artifacts parsed: {len(artifacts)}")
    print(f"Domain objects found:   {domain_count}")
    print()

    if domain_artifacts:
        # Group by domain type
        by_type: dict[str, list] = {}
        for a in domain_artifacts:
            dtype = a.spec_metadata["domain"]
            by_type.setdefault(dtype, []).append(a)

        for dtype, items in sorted(by_type.items()):
            print(f"  [{dtype}]")
            for a in items:
                title = a.spec_metadata.get("title", a.title or "(no title)")
                print(f"    {a.id}: {title}")
            print()

    # Check for FRs missing domain that might need one
    non_domain_frs = [
        a
        for a in artifacts
        if a.id
        and a.id.startswith("FR-")
        and (not a.spec_metadata or not a.spec_metadata.get("domain"))
    ]
    if non_domain_frs:
        print(f"FRs without domain type ({len(non_domain_frs)}):")
        for a in non_domain_frs:
            title = (
                a.spec_metadata.get("title", a.title)
                if a.spec_metadata
                else "(no metadata)"
            )
            print(f"  {a.id}: {title}")
        print()

    if domain_count == 0:
        print("WARNING: No domain objects found!")
        return 1

    print(f"OK: {domain_count} domain objects verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
