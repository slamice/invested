var React = require('react');
var ReactDOM = require('react-dom');

import App from './App.jsx';

require('../css/main.css');

ReactDOM.render(
    <App/>, document.getElementById('root'));

var $ = require('jquery');
console.log($("#root"));
