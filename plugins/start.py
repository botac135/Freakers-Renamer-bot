from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert 

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_text(text =f"""
	Hello {message.from_user.first_name }
	__I am file renamer bot, Please sent any telegram 
	**Document Or Video** and enter a new filename to rename it__
	""",reply_to_message_id = message.message_id ,  
	reply_markup=InlineKeyboardMarkup([[
          InlineKeyboardButton("𝑴𝒐𝒗𝒊𝒆𝒔" ,url="https://t.me/freakersmovies"), 
	  InlineKeyboardButton("𝑺𝒆𝒓𝒊𝒆𝒔", url="https://t.me/freakersseeies")
          ],[
          InlineKeyboardButton("𝑶𝒘𝒏𝒆𝒓 𝑶𝒇 𝑴𝒆", url="https://t.me/naughty_nonsense")
          ]]
          )
        )



@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       media = await client.get_messages(message.chat.id,message.message_id)
       file = media.document or media.video or media.audio 
       filename = file.file_name
       filesize = humanize.naturalsize(file.file_size)
       fileid = file.file_id
       await message.reply_text(
       f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {filesize}"""
       ,reply_to_message_id = message.message_id,
       reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("𝑹𝒆𝒏𝒂𝒎𝒆 ✍️",callback_data = "rename")
       ,InlineKeyboardButton("𝑪𝒂𝒏𝒄𝒆𝒍 🗑️",callback_data = "cancel")  ]]))
