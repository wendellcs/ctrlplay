const mongoose = require('mongoose')

const gameSchema = new mongoose.Schema({
    nome: { type: String },
    genero: { type: String },
    ano: { type: Number },
    empresa: { type: String },
    preco: { type: Number },
    createdAt: { type: Date, default: Date.now }
})

console.log()

const Game = mongoose.model('Game' , gameSchema);

module.exports = Game