<script>
export default {
  data() {
    return {
      systems: [],
      category: [],
      services: [],
      formsService:[],
      competenceTeams:[],
      modal:{},
      showDetais: 0,
      showDetaisCat: 0,
      showDetaisSystem: 0,
      showDetaisService: 0
    }
  },
  methods: {
    getDetailCategory(id) {
      if (this.showDetais != id) {

        return this.$axios
            .get(this.$HttpApiAddress + 'category/' + id + '/system')
            .then((response) => {
              this.category = response.data.result;
              return this.showDetais = id
            })
            .catch((error) => console.log(error))
      }

    },
    getDetailSystem(id) {
      if (this.showDetaisSystem != id) {
        this.$axios
            .get(this.$HttpApiAddress + 'system/' + id + '/service')
            .then((response) => {
              this.services = response.data.result
              return this.showDetaisSystem = id
            })
            .catch((error) => console.log(error))
      }
    },
    getDetailService(id) {
      this.showDetaisService = id;
    },
    getformsService(id) {
      this.$axios
          .get(this.$HttpApiAddress + 'forms/system_service/' + id)
          .then((response) => {
            this.formsService = response.data.result
          })
          .catch((error) => console.log(error))
    },
    getTeamsService(id) {
      this.$axios
          .get(this.$HttpApiAddress + 'teams/' + id + '/competence_teams')
          .then((response) => {
            this.competenceTeams = response.data.result
          })
          .catch((error) => console.log(error))
    },
    getform(id) {
      this.$axios
          .get(this.$HttpApiAddress + 'forms/' + id)
          .then((response) => {
            this.modal = response.data
          })
          .catch((error) => console.log(error))
    }

  },
  mounted() {
    //Получаем список услуг первого уровня
    console.log();
    this.$axios
        .get(this.$HttpApiAddress + 'category/?page=0&limit=50')
        .then((response) => {
          this.systems = response.data.result
        })
        .catch((error) => console.log(error))
  }
}
</script>

<template>
  <div v-if="systems == 0">
    <p>Записи отсутствуют</p>
  </div>
  <div class="col-prod-elem" :data-id="i.id" data-type="category" v-for="i in systems"
       v-on:click="getDetailCategory(i.id)">
    <div class="col-md-12 col-sm-12 col-lg-12 col-xs-12 item-list-products"
         data-percentid="" data-type="Credit">
      <div class="col-md-2 col-lg-2 col-sm-2 col-xl-2 col-xs-6 ">
        <div class="b-mission-ava logo-credits-item">
          <img style="height: 25px" src="/src/assets/shards/image/icn_vrabote.svg">
          <p></p>
          <span style="font-size: 16px">{{ i.name }}</span>
        </div>
      </div>
      <div class="col-md-10 col-lg-10 col-sm-10 col-xl-10 col-xs-6 name-js-css">
        <h6 class="item-title-product" style="font-size: 13px; text-align: left">{{ i.description }}
          <div v-on:click="getDetailCategory(0)" v-if="this.showDetais == i.id" style="float: right;padding: 15px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-chevron-up"
                 viewBox="0 0 16 16">
              <path fill-rule="evenodd"
                    d="M7.646 4.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1-.708.708L8 5.707l-5.646 5.647a.5.5 0 0 1-.708-.708l6-6z"/>
            </svg>
          </div>
        </h6>
      </div>

    </div>


    <div v-if="i.id == this.showDetais" class="col-md-12 col-sm-12 col-lg-12 col-xs-12 detals-product-credit"
         style="display: block;">
      <div class="tabs ui-tabs ui-corner-all ui-widget ui-widget-content">
        <ul class="nav nav-tabs ui-tabs-nav ui-corner-all ui-helper-reset ui-helper-clearfix ui-widget-header">
          <li class="active">
            <a href="#first-tab-content" data-toggle="tab">Системы</a></li>
<!--          <li><a href="#second-tab-content" data-toggle="tab">Аналитика</a></li>
          <li><a href="#fifth-tab-content" data-toggle="tab">Описание</a></li>-->
          <li style="float: right">
            <a href="#" style="background-color: #eee;font-weight: bold;cursor: default;pointer-events: none;" >{{ i.name }}</a>
          </li>
        </ul>


        <div class="tab-content">
          <div id="first-tab-content" class="tab-pane fade in active">
            <!--            <h3>Категории услуги 2 уровень</h3>-->

            <div class="container"
                 style="margin-top: 50px"
            >
              <div class="lonload " style="border-left: 2px solid #7079dc;">

                <div class="center-block list-products-block" style="">
                  <div class="col-md-12 col-sm-12 col-lg-12 col-xs-12 hidden-xs full-list-products">
                    <div class="col-md-2 col-lg-2 col-sm-2 col-xl-2 title-table">Название</div>
                    <div class="col-md-2 col-lg-2 col-sm-2 col-xl-2 title-table">Описание</div>
                  </div>

                  <div id="productsMain" style="width: 100%">
                    <div v-if="this.category == 0">
                      <p>Записи отсутствуют</p>
                    </div>
                    <div class="col-prod-elem" v-for="program in this.category"
                         v-on:click="getDetailSystem(program.id)">
                      <div class="col-md-12 col-sm-12 col-lg-12 col-xs-12 item-list-products"
                           data-percentid="" data-type="Credit">
                        <div class="col-md-2 col-lg-2 col-sm-2 col-xl-2 col-xs-6 ">
                          <div class="b-mission-ava logo-credits-item">
                            <span style="font-size: 16px;font-weight: bold;">{{ program.name }}</span>
                          </div>
                        </div>
                        <div class="col-md-10 col-lg-10 col-sm-10 col-xl-10 col-xs-6 name-js-css">
                          <h6 class="item-title-product" style="font-size: 13px; text-align: left">
                            {{ program.description }}
                            <div v-on:click="getDetailSystem(0)" v-if="this.showDetaisSystem == i.id" style="float: right;padding: 15px;">
                              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-chevron-up"
                                   viewBox="0 0 16 16">
                                <path fill-rule="evenodd"
                                      d="M7.646 4.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1-.708.708L8 5.707l-5.646 5.647a.5.5 0 0 1-.708-.708l6-6z"/>
                              </svg>
                            </div>
                          </h6>

                        </div>

                      </div>

                      <div v-if="program.id == showDetaisSystem"
                           class="col-md-12 col-sm-12 col-lg-12 col-xs-12 detals-product-credit" id="101"
                           style="display: block;">
                        <div class="tabs ui-tabs ui-corner-all ui-widget ui-widget-content">
                          <ul class="nav nav-tabs ui-tabs-nav ui-corner-all ui-helper-reset ui-helper-clearfix ui-widget-header">
                            <li class="active">
                              <a href="#first-tab-content1" data-toggle="tab">Услуги</a></li>

                            <li style="float: right">
                              <a href="#" style="background-color: #eee; font-weight: bold;pointer-events: none;" >{{ program.name }}</a>
                            </li>
                            <li style="float: right">
                              <a href="#" style="background-color: #eee;pointer-events: none;" >{{ i.name }}</a>
                            </li>
                          </ul>

                          <div class="tab-content">
                            <div id="first-tab-content1" class="tab-pane fade in active">
                              <!--                              <h3>Категории услуги Уровень 3</h3>-->

                              <div class="container" style="margin-top: 50px">
                                <div class="lonload " style="border-left: 2px solid #7edc70;">

                                  <div class="center-block list-products-block">
                                    <div class="col-md-12 col-sm-12 col-lg-12 col-xs-12 hidden-xs full-list-products">
                                      <div class="col-md-2 col-lg-2 col-sm-2 col-xl-2 title-table">Название</div>
                                      <div class="col-md-2 col-lg-2 col-sm-2 col-xl-2 title-table">Описание</div>
                                    </div>

                                    <div id="productsMain" style="width: 100%">
                                      <div v-if="this.services.length == 0">
                                        <p>Записи отсутствуют</p>
                                      </div>
                                      <div class="col-prod-elem"
                                           v-on:click="getDetailService(serice.service.id)"
                                           v-for="serice in this.services">
                                        <div class="col-md-12 col-sm-12 col-lg-12 col-xs-12 item-list-products"
                                             data-percentid="" data-type="Credit">
                                          <div class="col-md-2 col-lg-2 col-sm-2 col-xl-2 col-xs-6 ">
                                            <div class="b-mission-ava logo-credits-item">
                                              <p></p>
                                              <span style="font-size: 16px;font-weight: bold;">{{ serice.service.name }}</span>
                                            </div>
                                          </div>
                                          <div class="col-md-10 col-lg-10 col-sm-10 col-xl-10 col-xs-6 name-js-css">
                                            <h6 class="item-title-product" style="font-size: 13px; text-align: left">
                                              {{ serice.service.description }}</h6>
                                          </div>

                                        </div>


                                        <div v-if="serice.service.id == this.showDetaisService"
                                             class="col-md-12 col-sm-12 col-lg-12 col-xs-12 detals-product-credit"
                                             id="101"
                                             style="display: block;">
                                          <div class="tabs ui-tabs ui-corner-all ui-widget ui-widget-content">
                                            <ul class="nav nav-tabs ui-tabs-nav ui-corner-all ui-helper-reset ui-helper-clearfix ui-widget-header">
                                              <li class="active">
                                                <a href="#first-tab-content2" data-toggle="tab">Описание</a></li>
                                              <li><a href="#second-tab-content2" @click="getTeamsService(serice.service.id)" data-toggle="tab">Исполнители</a></li>
                                              <li><a href="#fifth-tab-content2" @click="getformsService(serice.service.id)" data-toggle="tab">Формы</a></li>

                                              <li style="float: right">
                                                <a href="#" style="background-color: #eee; font-weight: bold;pointer-events: none;" >{{ serice.service.name }}</a>
                                              </li>
                                              <li style="float: right">
                                                <a href="#" style="background-color: #eee;pointer-events: none;" >{{ program.name }}</a>
                                              </li>
                                              <li style="float: right">
                                                <a href="#" style="background-color: #eee;pointer-events: none;" >{{ i.name }}</a>
                                              </li>
                                            </ul>

                                            <div class="tab-content">
                                              <div id="first-tab-content2" class="tab-pane fade in active">
                                                <h3>{{ serice.service.name }}</h3>
                                                <p>{{ serice.service.description }}</p>

                                                <div class="container" style="margin-top: 30px">
                                                  <div class="row">
                                                    <div class="col-md-4">
                                                      <table class="table " style="width: 100%;">
                                                        <tr style="text-align: left">
                                                          <td><span style="text-align: left">Время поддрежки сервиса </span></td>
                                                          <td><span>c <b>{{ serice.service.start_support_time }}</b></span> до <span class="text-character">{{ serice.service.end_support_time }}</span> МСК</td>
                                                        </tr>
                                                        <tr style="text-align: left">
                                                          <td><span style="text-align: left">Время предоставления услуги </span></td>
                                                          <td><span class="text-character">{{ serice.service.time_to_request }}</span> часа </td>
                                                        </tr>
                                                        <tr style="text-align: left">
                                                          <td><span style="text-align: left">Способ предоставления услуги</span></td>
                                                          <td><span class="text-character">{{ serice.service.method_providing }}</span></td>
                                                        </tr>
                                                      </table>
                                                    </div>

                                                    <div class="col-md-4">
                                                      <table class="table" style="width: 100%;">
                                                        <tr style="text-align: left">
                                                          <td><span style="text-align: left">Владелец услуги </span></td>
                                                          <td><span class="text-character">{{ serice.owner.name }}</span></td>
                                                        </tr>
                                                        <tr style="text-align: left">
                                                          <td><span style="text-align: left">Департамент </span></td>
                                                          <td><span class="text-character" style="text-align: left">{{ serice.owner.department }}</span></td>
                                                        </tr >
                                                        <tr style="text-align: left">
                                                          <td><span style="text-align: left">Управлени </span></td>
                                                          <td><span class="text-character" style="text-align: left">{{ serice.owner.management }}</span></td>
                                                        </tr>
                                                        <tr style="text-align: left">
                                                          <td><span style="text-align: left">Отдел </span></td>
                                                          <td><span class="text-character" style="text-align: left">{{ serice.owner.divizion }}</span></td>
                                                        </tr>
                                                        <tr style="text-align: left">
                                                          <td><span style="text-align: left">email </span></td>
                                                          <td><span class="text-character" style="text-align: left">{{ serice.owner.email }}</span></td>
                                                        </tr>
                                                      </table>

                                                    </div>

                                                    <div class="col-md-3">
                                                      <table class="table " style="width: 100%;">
                                                        <tr style="text-align: left">
                                                          <td><span style="text-align: left">Календарь поддержки</span></td>
                                                          <td><span class="text-character">{{ serice.calendar.name }}</span>
                                                            <p style="color: #737373;">{{ serice.calendar.description }}</p>
                                                          </td>
                                                        </tr>
                                                      </table>
                                                    </div>

                                                  </div>
                                                </div>


                                              </div>

                                              <div id="second-tab-content2" class="tab-pane fade">
                                                <div v-for="competence in this.competenceTeams" class="competention-box col-md-3">
                                                  <p style="text-align: left; font-weight: bold">{{ competence.role_name }}</p>
                                                  <p style="text-align: left">Плановое время {{ competence.plan_time }} </p>
                                                  <p style="text-align: left">Время начала поддержки {{ competence.start_support_time }} </p>
                                                  <p style="text-align: left">Время окончания поддержки {{ competence.end_support_time }} </p>
                                                </div>
                                              </div>
                                              <div id="third-tab-content2" class="tab-pane fade">
                                                <h3>Третий заголовок</h3>
                                                ert
                                              </div>
                                              <div id="fourth-tab-content2" class="tab-pane fade">
                                                <h3>Четвертый заголовок</h3>
                                                <p>
                                                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                                                  eiusmod tempor
                                                  incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
                                                  quis
                                                  nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
                                                  consequat.
                                                </p>
                                              </div>
                                              <div id="fifth-tab-content2" class="tab-pane fade">
                                                <h3>Формы</h3>

                                                <div v-for="form in this.formsService" style="text-align: left; margin-top: 20px">
                                                  <button class="btn btn-default" @click="getform(form.form_id)" data-toggle="modal" data-target="#modal-example" target="_blank">{{ form.form_name }}</button>
                                                </div>
                                              </div>
                                            </div>

                                          </div>
                                        </div>


                                      </div>

                                    </div>
                                  </div>
                                </div>
                              </div>


                            </div>

                            <div id="second-tab-content1" class="tab-pane fade">
                              <h3>Второй заголовок</h3>
                              <p>
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
                                incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
                                nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                              </p>
                            </div>
                            <div id="third-tab-content1" class="tab-pane fade">
                              <h3>Третий заголовок</h3>
                              <p>
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
                                incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
                                nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                              </p>
                            </div>
                            <div id="fourth-tab-content1" class="tab-pane fade">
                              <h3>Четвертый заголовок</h3>
                              <p>
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
                                incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
                                nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                              </p>
                            </div>
                            <div id="fifth-tab-content1" class="tab-pane fade">
                              <h3>Пятый заголовок</h3>
                              <p>
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
                                incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
                                nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                              </p>
                            </div>
                          </div>

                        </div>
                      </div>

                    </div>

                  </div>
                </div>
              </div>
            </div>


          </div>
          <div id="second-tab-content" class="tab-pane fade">
            <h3>Второй заголовок</h3>
            <p>
              Lorem ipsum dolor sit amet
            </p>
          </div>
          <div id="third-tab-content" class="tab-pane fade">
            <h3>Третий заголовок</h3>
            <p>
              Lorem ipsum dolor sit amet
            </p>
          </div>
          <div id="fourth-tab-content" class="tab-pane fade">
            <h3>Четвертый заголовок</h3>
            <p>
              Lorem ipsum dolor sit amet
            </p>
          </div>
          <div id="fifth-tab-content" class="tab-pane fade">
            <h3>Пятый заголовок</h3>
            <p>
              Lorem ipsum dolor sit amet
            </p>
          </div>
        </div>

      </div>
    </div>

    <div class="modal fade" id="modal-example" tabindex="-1" role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <!-- заголовок -->
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Закрыть">
              <span aria-hidden="true">&times;</span>
            </button>
            <h4 class="modal-title">{{ this.modal.form_name }}</h4>
          </div>
          <!-- содержимое -->
          <div class="modal-body">
            <p style="text-align: left">
              Название формы: <a :href="'https://pyrus.sovcombank.ru/t#id'+this.modal.form_id" target="_blank">{{ this.modal.form_name }}</a>
            </p>
          </div>
          <!-- подвал -->
          <div class="modal-footer">
            <button type="button" class="btn btn-primary" data-dismiss="modal">Закрыть</button>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<style scoped>
 .text-character {
   font-weight: bold;
 }
 .competention-box {
   box-shadow: 0 0 20px rgba(0,0,0,.1);
   border-radius: 7px;
   border: 1px solid #0000001f;
   padding: 15px;
 }
 .nav-tabs>li.active>a, .nav-tabs>li.active>a:focus, .nav-tabs>li.active>a:hover {
   color: #555;
   cursor: default;
   background-color: #fff;
   border: 1px solid #ddd;
   border-color: transparent;
   margin-bottom: -1px;
   padding-bottom: 1px;
   border-bottom: 2px solid #7079dc;
   transition: border-bottom .3s ease;
   min-height: 35px;
   padding-bottom: 10px;
 }
 td, th {
   padding: 10px;
   text-align: left;
   border: 1px solid;
 }
</style>