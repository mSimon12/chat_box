import streamlit as st

COLOR_SENT = '#DCF8C6'
COLOR_RECEIVED = '#DDDDDD'

def chat_message(message, author, time, sent_by_me=True):
    """
    Renders chet message style.

    Args:
        message (str): The content of the message.
        author (str): The name of the message sender.
        time (str): The timestamp of the message.
        sent_by_me (bool): True if the message was sent by the current user (align right), False otherwise (align left).
    """

    if sent_by_me:
        alignment = 'flex-end'
        text_align = 'right'
        author_color = '#075E54'
        bg_color = COLOR_SENT
        margin_style = 'margin-left: auto;'
    else:
        alignment = 'flex-start'
        text_align = 'left'
        author_color = '#444444'
        bg_color = COLOR_RECEIVED
        margin_style = 'margin-right: auto;'

    html_code = f"""
    <div style="display: flex; justify-content: {alignment}; margin-bottom: 8px;">
        <div style="background-color: {bg_color}; border-radius: 10px; padding: 8px 12px; max-width: 70%; {margin_style}; box-shadow: 0 1px 0.5px rgba(0, 0, 0, 0.13);">
            <div style="font-weight: bold; font-size: 0.85em; color: {author_color}; text-align: {text_align};">{author}</div>
            <div style="font-size: 1em; color: #000000; text-align: {text_align}; word-wrap: break-word;">{message}</div>
            <div style="font-size: 0.7em; color: #888; margin-top: 4px; text-align: {text_align};">{time}</div>
        </div>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)
