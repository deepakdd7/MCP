# MCP STDIO
1. MCP Cli Server
   
   ```
   # cd /root/MCP/MCP-Demo
   # uv init mcp_cli_server
   # cd mcp_cli_server
   # uv venv
   # source .venv/bin/activate
   # uv add "mcp[cli]"
   # uv pip list
   # vi mcp_cli_server.py
   ```
   
2. MCP Cli Client

   ```
   # cd /root/MCP/MCP-Demo
   # uv init mcp_cli_client
   # cd mcp_cli_client
   # uv venv
   # source .venv/bin/activate
   # uv add mcp python-dotenv anthropic
   # uv pip list
   # vi mcp_cli_client.py
   ```

3. Execute MCP Server and Client

   ```
   # cd /root/MCP/MCP-Demo/mcp_cli_client
   # source .venv/bin/activate
   # vi /root/MCP/MCP-Demo/mcp_cli_server/mcp_cli_server.py
   # uv run ./mcp_cli_client.py /root/MCP/MCP-Demo/mcp_cli_server/mcp_cli_server.py
   ```

4. Questions

   * Add number 2 and 5
   * Multiply number 3 and 5

# MCP Streamable-HTTP

1. MCP Log Server Install

   ```
   # cd /root/MCP/MCP-Demo/mcp_log_server
   # uv init mcp_log_server
   # cd mcp_log_server
   # uv venv
   # source .venv/bin/activate
   # uv add mcp "mcp[cli]" fastmcp
   # uv pip list
   # vi mcp_log_server.py
   ```
   
2. Execute MCP Server 

   ```
   # cd /root/MCP/MCP-Demo/mcp_log_server
   # source .venv/bin/activate
   # vi /root/MCP/MCP-Demo/mcp_log_server/mcp_log_server.py
   # uv run mcp_log_server.py  OR # python mcp_log_server.py 
   # netstat -nltp | grep 8000
   ```

3. MCP Client

   ```
   # git clone https://github.com/bsneed/claude-desktop-fedora.git   (Perform steps as per README file)
   
   # cat /root/.config/Claude/claude_desktop_config.json
     ----------------------------------------
     {
      "mcpServers": {
        "LogAnalyzerMCP": {
           "command": "npx",
           "args": [
             "mcp-remote",
             "http://localhost:8000/mcp"
           ]
       }
      }
     }
     ----------------------------------------

   # claude-desktop --no-sandbox
   ```
