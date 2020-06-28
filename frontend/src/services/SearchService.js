import axios from 'axios';

class SearchService {
    search(query) {
        return axios.get(`http://localhost:5000?query=${query}`);
    }
}

export default SearchService;