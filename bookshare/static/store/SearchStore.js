import Dispatcher from './Dispatcher';

var _store = ['haha', 'hehe', 'hihi'];

function getAll() {
  return _store;
}

var methods = {
  getAll: function() {
    return _store;
  }
};

export default methods
