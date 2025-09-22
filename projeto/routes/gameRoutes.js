const express = require('express')
const router = express.Router()
const Game = require('../controller/gameController')

router.get('/games/:id' , Game.getGame)
router.post('/games/' , Game.createGame)
router.patch('/games/:id' , Game.updateGame)
router.delete('/games/:id' , Game.deleteGame)

module.exports = router