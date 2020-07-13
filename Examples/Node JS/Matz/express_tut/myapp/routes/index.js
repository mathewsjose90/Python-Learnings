var express = require('express');
var router = express.Router();
var videodata = require('../video_data.json');

/* GET home page. */
router.get('/', function (req, res, next) {
  res.render('index', { 'name': 'Mathews', 'videodata': videodata });
});

module.exports = router;
