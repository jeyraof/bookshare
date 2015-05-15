import React from 'react/addons';
import SearchStore from '../store/SearchStore';


var HelloMessage = React.createClass({
  render: function() {
    return <div>Hello {this.props.name}</div>;
  }
});

React.render(<HelloMessage name="John" />, document.getElementById('r-content'));
