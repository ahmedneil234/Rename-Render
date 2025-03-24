from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from helper.database import db
import logging

@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    try:
        file = getattr(message, message.media.value)
        filename = file.file_name if hasattr(file, 'file_name') else 'Not Available'
        filesize = file.file_size if hasattr(file, 'file_size') else 0
        
        try:
            text = f"""**__What do you want me to do with this file?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
            buttons = [[ InlineKeyboardButton("📝 RENAME", callback_data="rename") ],
                      [ InlineKeyboardButton("✖️ CANCEL", callback_data="cancel") ]]
            await message.reply_text(
                text=text,
                reply_to_message_id=message.id,
                reply_markup=InlineKeyboardMarkup(buttons)
            )
            logging.info(f"Rename request received for file: {filename}")
        except Exception as e:
            logging.error(f"Error in rename_start: {e}")
            await message.reply_text("An error occurred. Please try again later.")
            
    except Exception as e:
        logging.error(f"Main error in rename_start: {e}")
        await message.reply_text("Sorry, I couldn't process this file. Please try again.")

@Client.on_message(filters.private & filters.reply)
async def refunc(client, message):
    try:
        reply_message = message.reply_to_message
        if (reply_message.reply_markup) and isinstance(reply_message.reply_markup, ForceReply):
            new_name = message.text 
            await message.delete() 
            msg = await client.get_messages(message.chat.id, reply_message.id)
            file = msg.reply_to_message
            media = getattr(file, file.media.value)
            if not "." in new_name:
                if "." in media.file_name:
                    extn = media.file_name.rsplit('.', 1)[-1]
                else:
                    extn = "mkv"
                new_name = new_name + "." + extn
            await reply_message.delete()
            
            # Add logging
            logging.info(f"Renaming file to: {new_name}")
            
            # Continue with your rename process...
            
    except Exception as e:
        logging.error(f"Error in refunc: {e}")
        await message.reply_text("An error occurred during renaming. Please try again.")