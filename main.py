
TOKEN = "6845117408:AAF6NcMKIcr85E5atE7MNdsYfpo15UO__nE"  # فقط لخداع بعض الاستضافات

from telethon.sync import TelegramClient, events
import asyncio

# بيانات الحساب
api_id = 29438084
api_hash = '1cb2830a96e3d8cc3b00a235c6d332bc'
session_name = 'session_name'

# القنوات
source_channel = 'https://t.me/secret_solutionYT'
target_channel = 'https://t.me/softwar_quotex'

client = TelegramClient(session_name, api_id, api_hash)

async def main():
    await client.start()
    print("✅ تم تسجيل الدخول.")

    @client.on(events.NewMessage(chats=source_channel))
    async def handler(event):
        try:
            await client.send_message(target_channel, event.message)
            print(f"📤 تم نسخ الرسالة رقم {event.message.id}")
        except Exception as e:
            print(f"❌ خطأ أثناء الإرسال: {e}")

    print("🚀 السكربت شغال الآن وينسخ تلقائيًا...")
    await asyncio.Event().wait()

with client:
    client.loop.run_until_complete(main())
