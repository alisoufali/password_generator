from cli import cli
from password_generator import generate_password


if __name__ == "__main__":
    args = cli.parse_args()
    password = generate_password(
        length=args.length, use_upper=args.upper, use_lower=args.lower,
        use_digit=args.digit, use_punctuation=args.punc
    )
    print(password)
