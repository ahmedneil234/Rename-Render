@Client.on_callback_query(filters.regex('rename'))
async def rename(bot, update):
    try:
        user_id = update.message.chat.id
        date = update.message.date
        await update.message.delete()
        await update.message.reply_text("__𝙿𝚕𝚎𝚊𝚜𝚎 𝙴𝚗𝚝𝚎𝚛 𝙽𝚎𝚠 𝙵𝚒𝚕𝚎𝙽𝚊𝚖𝚎...__",	
        reply_to_message_id=update.message.reply_to_message.id,  
        reply_markup=ForceReply(True))
    except Exception as e:
        logging.error(f"Rename callback error: {e}")
        await update.message.reply_text("Error occurred. Please try again.")