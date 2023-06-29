import argparse

from piishield import PIIShield


def main():
    parser = argparse.ArgumentParser(
        prog="PIIShield",
        description="PIIShield parses an audio or video file and automatically redacts PII data",
    )

    parser.add_argument("-i", "--input", dest="input", help="the video file to bleep")

    parser.add_argument(
        "-o", "--output", dest="output", help="the destination output file path"
    )

    args = parser.parse_args()

    PIIShield(input=args.input)
