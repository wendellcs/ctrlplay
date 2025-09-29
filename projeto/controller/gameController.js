const Game = require('../models/jogos')

const getGame = async (req , res) => {
    try {
        const {id} = req.params
        const game = await Game.findById(id)

        if(!game) {
            return res.status(404).json({
                error: "Jogo não encontrado"
            })
        }

        res.json(game)
    } catch (e){
        res.status(500).json({ error: "Erro no servidor" })
    }
}

const createGame = async (req , res) => {
    try {
        const { nome ,ano , empresa , genero, preco } = req.body
        const newGame = new Game({nome, empresa, ano , genero , preco})
        await newGame.save()
        res.status(201).json(newGame)
    } catch (e) {
        res.status(500).json({
            error: "Erro ao criar o jogo"
        })
    }
}

const updateGame = async (req , res) => {
    try {
        const {id} = req.params
        const game = await Game.findById(id)

        if(!game) {
            return res.status(404).json({
                error: "Jogo não encontrado"
            })
        }

        res.json(game)
    } catch (e){
        res.status(500).json({ error: "Erro no servidor" })
    }
}

const deleteGame = async (req , res) => {
     try {
        const {id} = req.params
        const deletedGame = await Game.findByIdAndDelete(id)

        if (!deletedGame){
            return res.status(404).json({
                error: 'Jogo não encontrado'
            })
        }

        res.json({message: "Jogo excluído com sucesso"})
    } catch (e){
        res.status(500).json({ error:"Erro ao excluir o jogo" })
    }
}

module.exports = {createGame, updateGame, deleteGame, getGame}