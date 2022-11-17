import os
import sys
import yaml

def main():
    with open("examples/input/sli-description-ratio-metrics.yaml") as f:
        contents = yaml.safe_load(f)

    print(contents['apiVersion'])


if (__name__ == "__main__"):
    main()
