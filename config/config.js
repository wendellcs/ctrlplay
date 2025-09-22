const mongoose = require('mongoose')

const connectDB = async() => {
    try {
        // Faz a conexão com o banco de dados
        await mongoose.connect('mongodb://localhost:27017/jogosDB')
        console.log('MongoDB conectado!')
    } catch (e){
        console.error('Erro ao conectar ao MongoDB: ', e)
        // Encerra o processo
        process.exit(1)
    }
}

module.exports = connectDB