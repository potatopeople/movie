import axios from 'axios';

/*******全局配置********/
//POST请求头
axios.defaults.headers.post['Content-Type'] = 'application/json';
axios.defaults.headers.put['Content-Type'] = 'application/json';
let urls = 'http://localhost:5050/' //后端请求地址
export default {
  postHttp (url, datas) {
    return axios({
      url: urls + url,
      method: 'POST',
      data: JSON.stringify(datas)
    });
  },
  putHttp(url, datas) {
    return axios({
      url: urls + url,
      method: 'PUT',
      data: JSON.stringify(datas),
    });
  },
  getHttp (url, datas = '') {
    return axios({
      url: urls + url,
      method: 'GET',
      params: datas
    });
  },
  get_http_auth (url, datas = '',token) {
    return axios({
      url: urls + url,
      params: datas,
      method: 'GET',
      headers: {
        'Authorization': 'Basic ' + token
      }
    });
  },
  put_http_auth(url, datas = '', token) {
    return axios({
      url: urls + url,
      data: JSON.stringify(datas),
      method: 'PUT',
      headers: {
        'Authorization': 'Basic ' + token
      }
    });
  },
  del_http_auth(url, datas = '', token) {
    return axios({
      url: urls + url,
      method: 'DELETE',
      headers: {
        'Authorization': 'Basic ' + token
      }
    });
  },
  post_http_auth (url, datas = '', token) {
    return axios({
      url: urls + url,
      data: JSON.stringify(datas),
      method: 'POST',
      headers: {
        'Authorization': 'Basic ' + token
      }
    });
  },
}