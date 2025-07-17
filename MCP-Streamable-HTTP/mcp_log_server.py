import os
import mcp.types as types
from datetime import datetime
from mcp.server.fastmcp import FastMCP

# Check for root privileges needed to read system logs
if os.geteuid() != 0:
    raise PermissionError(
        "mcp_log_server.py requires root privileges to read /var/log/secure "
        "Please run as root (e.g., with sudo) "
        "or adjust file permissions."
    )

mcp = FastMCP(
    name="LogAnalyzerMCP",
    host="0.0.0.0",
    port=8000,
    streamable_http_path="/mcp"
)

## Register resources
@mcp.resource(
    uri="file:///var/log/secure",
    name="Secure Log",
    description="System security authentication log",
    mime_type="text/plain"
)
def secure_log() -> str:
    
    today_str = datetime.now().strftime("%b %d")  # e.g., "Jul 16"

    with open("/var/log/secure", "r") as f:
        lines = f.readlines()

    # Filter lines that start with today's date
    todays_lines = [line for line in lines if line.startswith(today_str)]

    return ''.join(todays_lines)

## Register prompt
@mcp.prompt(
    name="summarize-logs",
    description="Summarize important system and security events from logs"
)
def summarize_logs_prompt() -> list[types.PromptMessage]:
    secure = secure_log()
    user_message = f"""
    You are a Linux system assistant. Summarize the key security and system events from the following logs:

    --- /var/log/secure ---
    {secure}
    """
    return [
        types.PromptMessage(
            role="user",
            content=types.TextContent(type="text", text=user_message)
        )
    ]

## Register tool
@mcp.tool(
    name="login_events",
    description="Return SSH and terminal login success and failure logs"
)
async def login_events_tool() -> list[types.TextContent]:
    """
    Return SSH and terminal login success and failure entries from system logs.
    """
    
    prompt_messages = summarize_logs_prompt()
    return [msg.content for msg in prompt_messages if isinstance(msg.content, types.TextContent)]

if __name__ == "__main__":
    # Run the MCP server using Streamable HTTP transport on configured host and port
    mcp.run(transport="streamable-http")
