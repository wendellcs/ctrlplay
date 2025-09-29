const express = require('express')
const connectDB = require('./config/config')
const gameRoutes = require('./projeto/routes/gameRoutes')

const swaggerUi = require('swagger-ui-express');
const swaggerDocument = require('./docs/swagger.json');

const app = express()
connectDB()

app.use(express.json())
app.use('/api', gameRoutes)
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));

app.listen(3000, () => {
    console.log('Rodando o server na porta 3000')
})