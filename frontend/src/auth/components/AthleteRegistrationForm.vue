<template>
  <!--
      TODO @kike: Show a form with the following fields:
        - email: input type email, required
        - password: input type password, required, min 8 chars
        - repeat_password: input type password, required, must be the same as field password
        - first_name: input type text, required
        - last_name: input type text, required
        - country: input type text, required
        - date_of_birdth: datepicker, required
        - sport: input type text, required
        - sex: radio buttons. Options: male / female. Optional
        - Add labels
        - submit button
    -->
  <el-col :xs="24" :sm="12" :md="12" :lg="6" :xl="4" class="text-center">
    <h2>Athlete</h2>
    <el-form ref="form">
      <el-form-item required>
        <el-input placeholder="Email" type="email"></el-input>
      </el-form-item>
      <el-form-item required>
        <el-input placeholder="Password" type="password"></el-input>
      </el-form-item>
      <el-form-item required>
        <el-input placeholder="Repeat password" type="password"></el-input>
      </el-form-item>
      <el-form-item required>
        <el-input placeholder="First name" type="text"></el-input>
      </el-form-item>
      <el-form-item required>
        <el-input placeholder="Last name" type="text"></el-input>
      </el-form-item>
      <el-form-item required>
        <el-input placeholder="Country" type="text"></el-input>
      </el-form-item>
      <el-form-item required>
        <el-date-picker type="date" placeholder="Pick a date" style="width: 100%;"></el-date-picker>
      </el-form-item>
      <el-form-item required>
        <el-input placeholder="Sport" type="text"></el-input>
      </el-form-item>
      <el-form-item label="Sex" class="text-left">
        <el-radio-group>
          <el-radio label="Male"></el-radio>
          <el-radio label="Female"></el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" class="is-uppercase" @click="onSubmit">Register</el-button>
      </el-form-item>
    </el-form>
  </el-col>
</template>

<script>
  export default {
    name: 'AthleteRegistrationForm',
    components: {}
  }
</script>

<style type="scss" scoped>
</style>
