#!/usr/bin/env python3

# Written by Jakob Ruhe 2025
# Source: https://github.com/jakeru/nrfenv

import argparse
import json
import os
import logging
import subprocess


def parse_args():
    parser = argparse.ArgumentParser(
        description="Activates a nRF Connect toolchain environment",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "envfile", help="The environment file to use (typicaly named environment.json)"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose logging"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )
    for level in (logging.DEBUG, logging.INFO):
        logging.addLevelName(level, logging.getLevelName(level).lower())

    with open(args.envfile) as f:
        env_mods = json.load(f)
    newenv = os.environ.copy()
    base = os.path.dirname(os.path.abspath(args.envfile))
    for env_mod in env_mods["env_vars"]:
        key = env_mod["key"]
        values = env_mod.get("values", [env_mod.get("value", [])])
        type = env_mod.get("type")
        if type == "relative_paths":
            values = [os.path.join(base, v) for v in values]
        elif type == "string":
            pass
        else:
            raise ValueError(f"Unsupported for key '{key}': '{type}'")
        evt = env_mod.get("existing_value_treatment", "overwrite")
        if evt == "prepend_to":
            existing = newenv.get(key, "")
            logging.debug(f"Prepending key '{key}' with '{':'.join(values)}'")
            newenv[key] = ":".join(values + existing.split(":"))
        elif evt == "overwrite":
            logging.debug(f"Replacing key '{key}' with '{':'.join(values)}'")
            newenv[key] = ":".join(values)
        else:
            raise ValueError(
                f"Unsupported 'existing_value_treatment' for key '{key}': '{evt}'"
            )

    sh = os.getenv("SHELL", "sh")
    print(
        f"Running shell '{sh}' with new environment. Type 'exit' to return to the previous environment."
    )
    subprocess.run([sh], env=newenv)


if __name__ == "__main__":
    main()
