const express = require('express')
const connectDB = require('./config/config')
const gameRoutes = require('./projeto/routes/gameRoutes')
const app = express()
connectDB()

app.use(express.json())
app.use('/api', gameRoutes)

app.listen(3000, () => {
    console.log('Rodando o server na porta 3000')
})