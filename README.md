# ChatBox

A real-time chatting application built with WebSockets, featuring a FastAPI server for handling connections and a Streamlit client for the user interface.

## Features

- Real-time messaging via WebSockets
- Simple and intuitive Streamlit-based UI
- FastAPI server for scalable backend

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mSimon12/chat_box.git
   cd chat_box
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the project in editable mode:
   ```bash
   pip install -e .
   ```

## Usage

### Running the Server

Start the FastAPI server using Uvicorn:

```bash
uvicorn src.server.server:app --host 0.0.0.0 --port 8000 --reload
```

The server will be available at `http://localhost:8000` with WebSocket endpoint at `ws://localhost:8000/ws`.

### Running the Client

Launch the Streamlit client:

```bash
streamlit run src/app/chat_ui.py
```

Open the provided URL in your browser, enter a username, connect, and start chatting.

## Dependencies

- fastapi
- uvicorn
- streamlit
- streamlit-autorefresh
- websockets

## Development

To contribute or modify the code, ensure you have the dependencies installed and run the server/client as described.
