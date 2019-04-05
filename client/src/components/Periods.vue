<template>
  <div id="periods">
    <div class="columns is-mobile is-centered">
      <div class="column is-half">
        <form class="card">
          <div class="card-content">
            <div class="title is-4">Add Periods</div>
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <b-field label="Period Id" label-for="period-id"/>
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control">
                    <b-input
                      v-model="addPeriodsForm.periodId"
                      id="period-id"
                      type="text"
                      required
                      placeholder="Enter Period Id"
                    ></b-input>
                  </div>
                </div>
              </div>
            </div>
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <b-field label="Period Name" label-for="period-name"/>
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control">
                    <b-input
                      v-model="addPeriodsForm.periodName"
                      id="period-name"
                      type="text"
                      required
                      placeholder="Enter Period Name"
                    ></b-input>
                  </div>
                </div>
              </div>
            </div>
            <div class="field-body">
              <div style="padding:5px" class="field">
                <button class="button is-primary is-pulled-right" @click="onSubmit">Submit</button>
              </div>
            </div>
          </div>
        </form>
      </div>
      <div class="column ">
            <div class="card">
          <div class="card-content">
            <div class="title is-4">Current Periods</div>
            <b-table :data="periodsData" >
            <template slot-scope="props">
              <b-table-column
                field="periodId"
                label="Period Id"
                width="40"
                numeric
              >{{ props.row.periodId }}</b-table-column>
              <b-table-column
                field="periodName"
                label="Name"
                width="40"
                numeric
              >{{ props.row.periodName }}</b-table-column>
            </template>
          </b-table>
      </div>
      </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Periods",
  data() {
    return {
      periodsData: [],
      addPeriodsForm: {
        periodId: "",
        periodName: "",
      }
    };
  },
  methods: {
    getPeriods() {
      const path = "http://localhost:5000/periods";
      axios
        .get(path)
        .then(res => {
          this.periodsData = res.data.periods;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addPeriod(payload) {
      axios({
        method: "post",
        url: "http://localhost:5000/periods",
        data: {
          periodId: payload.periodId,
          periodName: payload.periodName,
        }
      })
        .then(function(response) {
          console.log(payload);
          this.success();
        })
        .catch(function(error) {
          console.log(error);
        });
      this.initForm();
    },
    initForm() {
      this.addPeriodsForm.periodId = "";
      this.addPeriodsForm.periodName = "";
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        periodId: this.addPeriodsForm.periodId,
        periodName: this.addPeriodsForm.periodName
      };
      this.addPeriod(payload);
    },
    success() {
      this.$toast.open({
        message: "Added successfully!",
        type: "is-success"
      });
    }
  },
  mounted() {},
  created() {
    this.getPeriods();
  }
};
</script>