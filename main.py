import click
import webdav_freezer.proc_handler


@click.command()
@click.option(
    "-f",
    "--config",
    default="config/arguments.py",
    help="TODO: Path to the configuration file. Defaults to config/arguments.py",
)
@click.option(
    "-t",
    "--test",
    type=bool,
    default=False,
    help="TODO: Test connections to webdav server and cold storage server",
)
@click.option(
    "-d",
    "--depth",
    type=int,
    help="Depth for folder crawling. -1 specifies full depth. Ex: Depth 3 with folder structure foo/bar/hello/world will not archive the contents of the folder world",
)
def main(config, test, depth):
    """
    Utility for pulling data from a WebDav server, compressing data, and moving snapshot to cold storage
    """
    # create new config object
    # create new webdav connection
    # create new cold storage connection
    # pass webdav connection and coldstorage to new proc_handler
    # report result
    return None

#     end_archive = None
#     threads = list()
#     # client = Client(args.WEBDAV_OPTIONS)
    client = WebDavClient()
    root_directory = client.list()[1:]
#     current_space_usage = 0 #in bytes
#     max_space_usage = 1000000000 # 1000 Gb
    print(root_directory[8] + "\n\n")
#     print(client.list(root_directory[0], get_info=True))

if __name__ == "__main__":
    main()
