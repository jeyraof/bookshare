import React from 'react/addons';
import $ from 'jQuery';
import URI from 'URIjs'

var BookListItem = React.createClass({
  render: function() {
    var emptyImage = "data:image/png;base64,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";
    var thumb = this.props.data.thumb || emptyImage;

    return (<div className="book">
      <div className="overlay">
        <div className="add">
          <a>
            <i className="ion-plus"></i>
            <p className="msg">내 책장으로</p>
          </a>
        </div>

        <div className="stock">
          <a>
            <i className="ion-heart"></i>
            <p className="msg">보고싶은 책</p>
          </a>
        </div>
      </div>
      <img className="cover" src={thumb}/>
      <h4 className="title" title={this.props.data.title}>{this.props.data.title}</h4>
      <p className="author">{this.props.data.author}</p>
    </div>);
  }
});

var BookList = React.createClass({
  render: function() {
    var bookNode = this.props.data.map((bookData) => {
      return <li><BookListItem data={bookData.fields}/></li>
    });

    return (<ul className="book-list">{bookNode}</ul>);
  }
});

var SearchList = React.createClass({
  getQueryString() {
    return new URI(window.location.search || '');
  },

  getInitialState() {
    var qsSet = this.getQueryString().search(true);

    return {
      inProcessing: false,
      bookList: [],
      page: 1,
      q: qsSet.q || null
    }
  },

  searchBook(keyword, page, success) {
    var qs = this.getQueryString();
    this.setState({inProcessing: true});
    $.ajax({
      type: "GET",
      url: "/api/v1/search" + qs.setSearch({
        page: page,
        q: keyword
      }),
      success: success.bind(this),
      complete: function() {this.setState({inProcessing: false})}.bind(this)
    })
  },

  componentWillMount() {
    var qsSet = this.getQueryString().search(true);

    this.searchBook(qsSet.q, 1, function(res) {
      if (res.ok) {
        this.setState({
          bookList: res.item,
          page: res.page
        });
      } else {
        alert(res.msg);
        history.go(-1);
      }
    }.bind(this));
  },

  searchMore() {
    var qsSet = this.getQueryString().search(true);
    this.searchBook(qsSet.q, this.state.page + 1, function(res) {
      this.setState((previous, props) => {
        return {
          bookList: previous.bookList.concat(res.item),
          page: res.page
        }
      });
    }.bind(this));
  },

  render() {
    var msg = this.state.inProcessing ? '로딩중' : '더 불러오기';
    var disabled = this.state.inProcessing ? 'disabled' : '';
    return(<div className="search-box">
      <BookList data={this.state.bookList}/>
      <div>
        <button className="more btn green" onClick={this.searchMore} disabled={disabled}>
        {msg}
        </button>
      </div>
    </div>);
  }
});

React.render(<SearchList/>, document.getElementById('r-content'));
