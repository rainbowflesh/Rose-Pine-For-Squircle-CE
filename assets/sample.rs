use anyhow::Result;
use axum::{routing::get, Router};

use diting_webapi::{configs::AppConfig, server};
use diting_webapi::msg_server;

#[tokio::main]
async fn main() -> Result<()> {
    let config = AppConfig::new()?;
    // debug!(?config);

    tokio::spawn(msg_server::start());
    server::launch(&config).await?;

    Ok(())
}
