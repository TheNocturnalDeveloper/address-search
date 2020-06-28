import React from 'react';
import SearchService from "services/SearchService"

import 'css/Search.css';

class Search extends React.Component {
    constructor(props) {
        super(props);
        this.searchService = new SearchService()
        this.state = {
            value: '',
            result: []
        };
        
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
  
    handleChange(event) {
        this.setState({value: event.target.value});
    }
  
    handleSubmit(event) {
        this.searchService.search(this.state.value).then(r => {
            this.setState({result : Object.entries(r.data)});
        }).catch(e => {
            alert("something went wrong while searching: " + e.message);
        });
        
        event.preventDefault();
    }
  
    render() {
      return (
            <div>
                <form className="search-form" onSubmit={this.handleSubmit}>
                   
                    <input type="text" value={this.state.value} onChange={this.handleChange} />
                    
                    <button>search</button>
                </form>
                <table className="result-table">
                    <thead>
                        <tr><th>property</th><th>value</th></tr>
                    </thead>
                    <tbody>
                        {
                            this.state.result.map((value, i) =>  
                                <tr key={i}>
                                    <td>{value[0]}</td>
                                    <td>{value[1]}</td>
                                </tr>
                            )
                        }
                    </tbody>
                </table>
            </div>
        );
    }
}
export default Search;