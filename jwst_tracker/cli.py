from __future__ import annotations

import click

from . import mast_client, catalog, plots


@click.group()
def main():
    """JWST data tracker command line interface."""


@main.command()
@click.option("--program", "program_id", help="JWST program ID to query.")
@click.option("--target", "target_name", help="Target name to query.")
@click.option("--radius", default="0.1 deg", show_default=True, help="Search radius around target.")
@click.option("--product", "product_substring", multiple=True, help="Filename substring to select products.")
@click.option("--download/--no-download", default=False, show_default=True)
def update(program_id, target_name, radius, product_substring, download):
    """Query JWST observations and update local catalog."""
    if not program_id and not target_name:
        raise click.UsageError("Provide either --program or --target")

    if program_id:
        obs_df = mast_client.query_by_program(program_id)
    else:
        obs_df = mast_client.query_by_target(target_name, radius=radius)

    combined = catalog.update_catalog(obs_df)
    click.echo(f"Catalog now has {len(combined)} unique observations.")

    if download:
        products = mast_client.get_products(obs_df, product_substrings=product_substring or None)
        from .download import download_products
        manifest = download_products(products)
        click.echo(f"Downloaded products; manifest: {manifest}")


@main.command("make-plots")
def make_plots():
    """Generate basic summary plots from the catalog."""
    plots.plot_counts_by_instrument()


if __name__ == "__main__":
    main()
