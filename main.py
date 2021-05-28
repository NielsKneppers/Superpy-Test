# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.

from arguments import arguments
from make_report import make_report
from buying_products import buy_product
from selling_products import sell_product
from advance_time import advance_date
from rich.console import Console


def main(args):
    args = arguments()
    if args.command == "report":
        make_report(args)
    elif args.command == "buy":
        buy_product(args)
    elif args.command == "sell":
        sell_product(args)
    elif args.command == "advance":
        advance_date(args)



if __name__ == "__main__":
    myconsole = Console()
    myconsole.print("-" * 80)

    args = arguments()
    main(args)

    myconsole.print("-" * 80)
    myconsole.print("# Arguments", args)
    myconsole.print("-" * 80)
