import os 
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    filters,
)
from dotenv import load_dotenv

load_dotenv()  # carrega as variáveis do .env

TOKEN = os.getenv("BOT_TOKEN")

print("Token carregado:", TOKEN)  # Para você ver se carregou

DUVIDA, ORACAO, DESABAFO = range(3)  # estados da conversa

# MENU PRINCIPAL - botões em ordem alfabética
def get_menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💻 Biblioteca digital", callback_data='biblioteca')],
        [InlineKeyboardButton("🔥 Desafios Devocionais", callback_data='desafio')],
        [InlineKeyboardButton("💜 Espaço para Desabafo", callback_data='desabafo')],
        [InlineKeyboardButton("🤔 Enviar dúvida", callback_data='duvida')],
        [InlineKeyboardButton("📅 Próximas aulas", callback_data='aulas')],
        [InlineKeyboardButton("🙏 Pedido de Oração", callback_data='oracao')],
        [InlineKeyboardButton("🎧 Playlist Teen", callback_data='playlist')],
        [InlineKeyboardButton("🧠 Quiz Bíblico", callback_data='quiz')],
        [InlineKeyboardButton("📚 Resumo da Aula", callback_data='resumo')],
        [InlineKeyboardButton("📖 Versículo da Semana", callback_data='versiculo')],
    ])

# BOTÃO VOLTAR
def get_voltar_keyboard():
    return InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Voltar ao menu", callback_data='voltar')]])

# SUBMENU DE PLAYLISTS (ordem alfabética)
def get_playlist_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🎶 Playlist - Coreano", callback_data='coreano')],
        [InlineKeyboardButton("🎶 Playlist - Espanhol", callback_data='espanhol')],
        [InlineKeyboardButton("🎶 Playlist - Inglês", callback_data='ingles')],
        [InlineKeyboardButton("🎶 Playlist - Mandarim", callback_data='mandarim')],
        [InlineKeyboardButton("🎶 Playlist - Português", callback_data='portugues')],
        [InlineKeyboardButton("⬅️ Voltar ao menu", callback_data='voltar')]
    ])

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌟 Olá! Seja bem-vindo(a) ao Gabi's Class 💜✨\n\nEstou aqui para te ajudar a crescer, aprender e se conectar com Deus de forma leve e divertida.\n\nEscolha uma das opções abaixo e bora começar! 👇",
        reply_markup=get_menu_keyboard()
    )

# BOTÕES
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == 'voltar':
        await query.edit_message_text("Você voltou ao menu inicial.", reply_markup=get_menu_keyboard())
        return ConversationHandler.END

    elif data == 'duvida':
        await query.edit_message_text("Envie aqui a sua dúvida e eu vou registrar para você!", reply_markup=get_voltar_keyboard())
        return DUVIDA

    elif data == 'aulas':
        texto = "📚 Próxima aula:\n- Dia: 07/09\n- 10-Maria: o que responder ao chamado de Deus?" #data da minha proxima aula
        await query.edit_message_text(texto, reply_markup=get_voltar_keyboard())

    elif data == 'biblioteca':
        texto = "📎 Materiais complementares para estudo:\n- Clique aqui para acessar: inserir link" #link da biblioteca digital
        await query.edit_message_text(texto, reply_markup=get_voltar_keyboard())

    elif data == 'playlist':
        await query.edit_message_text("🎧 Escolha uma playlist por idioma:", reply_markup=get_playlist_keyboard())

    elif data in ['coreano', 'espanhol', 'ingles', 'mandarim', 'portugues']:
        links = {
            'coreano': 'https://open.spotify.com/playlist/coreano',
            'espanhol': 'https://open.spotify.com/playlist/espanhol',
            'ingles': 'https://open.spotify.com/playlist/ingles',
            'mandarim': 'https://open.spotify.com/playlist/mandarim',
            'portugues': 'https://open.spotify.com/playlist/portugues'
        }
        idioma_nome = data.capitalize()
        texto = f"Aqui está a playlist em *{idioma_nome}* 🎵\n{links[data]}"
        await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=get_playlist_keyboard())

    elif data == 'versiculo':
        texto = "📖 *Versículo da Semana:*\n\n\"Confia no Senhor de todo o teu coração e não te estribes no teu próprio entendimento.\" (Provérbios 3:5)"
        await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=get_voltar_keyboard())

    elif data == 'quiz':
        texto = "🧠 *Quiz Bíblico em breve!*\nAguarde perguntas interativas para testar seus conhecimentos. 😉"
        await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=get_voltar_keyboard())

    elif data == 'resumo':
        texto = "📚 *Resumo da Última Aula:*\n\nTema: Mudar\nResumo: Mudar"
        await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=get_voltar_keyboard())

    elif data == 'desafio':
        texto = "🔥 *Desafio Devocional:*\n\nDurante 7 dias, reserve 5 minutos para orar e anotar o que Deus te mostrou em um caderno. Topa o desafio?"
        await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=get_voltar_keyboard())

    elif data == 'oracao':
        await query.edit_message_text("🙏 Envie seu pedido de oração. Estarei orando com você!", reply_markup=get_voltar_keyboard())
        return ORACAO

    elif data == 'desabafo': 
        await query.edit_message_text(
            "💜 Este é seu espaço seguro para desabafar.\n\n"
            "Fique à vontade para compartilhar o que estiver sentindo — aqui você será ouvido(a) com muito carinho e respeito.\n\n"
            "Quando quiser, clique em ⬅️ Voltar ao menu.",
            reply_markup=get_voltar_keyboard()
        )
        return DESABAFO

    return ConversationHandler.END

# RECEBE DÚVIDA
async def receber_duvida(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    user = update.message.from_user
    linha = f"Dúvida de {user.full_name} (@{user.username}): {texto}\n"

    with open("duvidas.txt", "a", encoding="utf-8") as file:
        file.write(linha)

    await update.message.reply_text("📩 Sua dúvida foi registrada. Obrigada!", reply_markup=get_menu_keyboard())
    return ConversationHandler.END

# RECEBE PEDIDO DE ORAÇÃO
async def receber_oracao(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    user = update.message.from_user
    linha = f"Pedido de oração de {user.full_name} (@{user.username}): {texto}\n"

    with open("oracoes.txt", "a", encoding="utf-8") as file:
        file.write(linha)

    await update.message.reply_text("🙏 Seu pedido foi registrado. Estarei orando por você!", reply_markup=get_menu_keyboard())
    return ConversationHandler.END

# RECEBE DESABAFO
async def receber_desabafo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    user = update.message.from_user
    linha = f"💬 Desabafo de {user.full_name} (@{user.username}): {texto}\n\n"

    with open("desabafos.txt", "a", encoding="utf-8") as file:
        file.write(linha)

    await update.message.reply_text(
        "🌟 Obrigado por confiar em mim e compartilhar seus sentimentos.\n"
        "Lembre-se: você não está sozinho(a) e é muito importante cuidar de você 💜\n\n"
        "Se precisar conversar mais, estarei sempre aqui!",
        reply_markup=get_menu_keyboard()
    )
    return ConversationHandler.END

# CANCELA OPERAÇÃO
async def cancelar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Operação cancelada. Voltando ao menu principal.", reply_markup=get_menu_keyboard())
    return ConversationHandler.END

# MAIN
def main():
    application = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start), CallbackQueryHandler(button_handler)],
        states={
            DUVIDA: [MessageHandler(filters.TEXT & ~filters.COMMAND, receber_duvida)],
            ORACAO: [MessageHandler(filters.TEXT & ~filters.COMMAND, receber_oracao)],
            DESABAFO: [MessageHandler(filters.TEXT & ~filters.COMMAND, receber_desabafo)],
        },
        fallbacks=[CommandHandler('cancel', cancelar)],
        per_user=True,
        per_chat=True,
    )

    application.add_handler(conv_handler)
    application.add_handler(CallbackQueryHandler(button_handler))

    print("Bot rodando...")
    application.run_polling()

if __name__ == "__main__":
    main()



#python bot_completo_g9.py

#.\venv\Scripts\Activate.ps1