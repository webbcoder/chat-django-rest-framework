import axios from 'axios'

export default () => {
        return axios.create({
                  baseURL: 'http://127.0.0.1:8000/api/v1/chat/',
                  headers: {'Authorization': `Token ${sessionStorage.getItem('auth_token')}`}
                });

}






