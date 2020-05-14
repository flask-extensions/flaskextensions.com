const instance = axios.create({
  baseURL: "http://localhost:8000/",
});

new Vue({
  el: "#app",
  data: {
    result: {},
    term: "",
  },
  async mounted() {
    const resp = await instance.get("extension/");
    this.result = resp.data;
  },
  filters: {
    truncate: function (text) {
      if (text.length > 80) return text.substring(0, 80) + " [...]";
      return text;
    },
  },
  methods: {
    async search() {
      const resp = await instance.get(`extension/?query=${this.term}`);
      this.result = resp.data;
    },
    async paginate(paginate_to) {
      const resp = await instance.get("extension/", {
        params: {
          page: paginate_to,
          per_page: this.result.page.page_size,
          query: this.term,
        },
      });
      this.result = resp.data;
    },
  },
});


// result = {
//   "page": {
//     "total": 0,
//     "page_size": 0,
//     "page": 0,
//     "previous": 0,
//     "next": 0,
//     "pages": 0
//   },
//   "items": [
//     {
//       "id": 0,
//       "name": "string",
//       "html_url": "string",
//       "description": "string",
//       "created_at": "2020-05-14T19:19:01.275Z",
//       "updated_at": "2020-05-14T19:19:01.275Z",
//       "stargazers_count": 0,
//       "forks_count": 0
//     }
//   ]
// }
