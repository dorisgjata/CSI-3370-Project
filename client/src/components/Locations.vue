<template>
  <div class="conatiner">
    <h1>{{ msg }}</h1>
    
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Locatons',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getLocations() {
      const path = 'http://localhost:5000/locations';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getLocations();
  },
};
</script>