const instance = axios.create({
  baseURL: `//${window.location.hostname}:8000/`,
  // baseURL: "http://161.35.57.225:8000/",
});

new Vue({
  el: "#app",
  data: {
    result: {},
    term: "",
    shotBy: "stars",
  },
  async mounted() {
    const resp = await instance.get("extension/");
    this.result = resp.data;
    this.adjustDate();
    this.changeShort();
  },
  filters: {
    truncate: function (text) {
      if (text != null) {
        if (text.length > 100) return text.substring(0, 100) + " [...]";
      } else {
        text = "";
      }
      return text;
    },
  },
  methods: {
    async search() {
      const resp = await instance.get(`extension/?query=${this.term}`);
      this.result = resp.data;
      this.adjustDate();
      this.changeShort();
    },
    async paginate(paginate_to) {
      const resp = await instance.get("extension/", {
        params: {
          page: paginate_to,
          per_page: this.result.page.page_size,
          query: this.term,
        },
      });
      console.log(resp.data);
      this.result = resp.data;
      this.adjustDate();
      this.changeShort();
    },
    changeShort() {
      this.shotBy = this.$refs.selectShort.value;
      switch (this.shotBy) {
        case "stars":
          this.shortByStars();
          break;
        case "forks":
          this.shortByForks();
          break;
        default:
          this.shortByName();
      }
    },
    shortByName() {
      this.result.items = this.result.items.sort((a, b) =>
        a.name.localeCompare(b.name)
      );
    },
    shortByStars() {
      this.result.items = this.result.items.sort(function (a, b) {
        return b.stargazers_count - a.stargazers_count;
      });
    },
    shortByForks() {
      this.result.items = this.result.items.sort(function (a, b) {
        return b.forks_count - a.forks_count;
      });
    },
    adjustDate() {
      Object.entries(this.result.items).forEach((value) => {
        let created_at = new Date(value[1].created_at.replace("T", " "))
          .toDateString()
          .slice(4, 15)
          .replace(" ", "-")
          .replace(" ", "-");
        value[1].created_at = created_at;

        let updated_at = new Date(value[1].updated_at.replace("T", " "))
          .toDateString()
          .slice(4, 15)
          .replace(" ", "-")
          .replace(" ", "-");
        value[1].updated_at = updated_at;
      });
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
