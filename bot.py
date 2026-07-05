from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TOKEN = "8651580410:AAGMX0bEPBj2KoLMPfALSziABbnE8ODVOnM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Click to Buy Premium ", callback_data="buy")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo="5921622830527221390.jpg",
        caption="""10K+ Hɪɢʜ Qᴜᴀʟɪᴛʏ Uɴsᴇᴇɴ Vɪᴅᴇᴏs Pᴀᴄᴋ ! \n
    🛒 Mᴏᴛʜᴇʀ & Sᴏɴ\n
    🛒 Sɪsᴛᴇʀ & Bʀᴏᴛʜᴇʀ\n
    🛒 Fᴀᴛʜᴇʀ & Dᴀᴜɢʜᴛᴇʀ \n
    ✅ RP 5000+\n
    ✅ CP 1500+\n
    \n
    Fᴜʟʟ Tʀᴜsᴛᴇᴅ | Dᴏɴ'ᴛ Tɪᴍᴇᴘᴀss\n
    \n
    • Pʀɪᴄᴇ : 99 Rᴜᴘᴇᴇs\n
    • Vᴀʟɪᴅɪᴛʏ - Lɪғᴇᴛɪᴍᴇ\n
    \n
    Buʏ Now 👇👇""",
        reply_markup=reply_markup
     )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "buy":
        await query.message.reply_photo(
            photo="5923443849416084823.jpg",
            caption="➖➖➖➖➖➖➖➖➖" "\n" "⚡ FLASH SALE: Only 8 Spots Left! 🔥" "\n""🍑 ONE-TIME PAYMENT: ₹99 ONLY!" "\n" "🔒 INSTANTLY GROUP ACCESS 🔥" "\n" "1️⃣ Scan QR & Pay ₹99" "\n" "2️⃣ And Send Payment ScreenShot"
        )
    context.user_data["awaiting_photo_reply"] = True
async def photo_reply_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get("awaiting_photo_reply"):
        await update.message.reply_text("🔍Your QR payment for Premium has been received and is under verification. ""\n" "Please allow some time while we complete the process")
        context.user_data["awaiting_photo_reply"] = None

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    # Only listen for PHOTO replies, ignore text
    app.add_handler(MessageHandler(filters.PHOTO, photo_reply_handler))
    app.run_polling()

if __name__ == "__main__":
    main()
