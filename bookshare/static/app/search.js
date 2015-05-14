var Book = React.createClass({
  render: function() {
    return (<div className="book">
      <div><img src={this.props.data.thumb}/></div>
      <div>{this.props.data.title}</div>
    </div>);
  }
});

var BookList = React.createClass({
  render: function() {
    var bookNode = this.props.data.map((bookData) => {
      return <li><Book data={bookData.fields}/></li>
    });

    return (<ul>{bookNode}</ul>);
  }
});

var SearchList = React.createClass({
  getInitialState: () => {
    return {
      bookListDAUM: [],
      bookListDB: []
    }
  },

  componentWillMount: function() {
    var queryString = window.location.search || '';
    $.ajax({
        type: "GET",
        url: "/api/v1/search" + queryString,
        success: function(res) {
            this.setState({
              bookListDB: JSON.parse(res.item.db),
              bookListDAUM: JSON.parse(res.item.daum)
            });
        }.bind(this)
    })
  },

  render: function() {
    return(<div>
      <BookList data={this.state.bookListDB}/>
    </div>);
  }
});

React.render(<SearchList/>, document.getElementById('r-content'));
