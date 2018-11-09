<template>
  <div>
    <template v-if="imageUrl">
      <img :src="imageUrl" alt="" class="preview">
      <button @click.prevent="deleteImage()">Delete</button>
    </template>
    <form v-else :class="['box', {'has-advanced-upload': dragAndDropCapable, 'is-uploading': uploading, 'is-error': hasError}]"
          method="post" action="" ref="fileform"
          enctype="multipart/form-data">
      <div class="box__input">
        <input class="box__file" type="file" name="files[]" id="file" @change="uploadFile($event)"/>
        <label for="file"><strong>Choose a file</strong><span class="box__dragndrop"> or drag it here</span>.</label>
        <button class="box__button" type="submit">Upload</button>
      </div>
    </form>
  </div>
</template>

<script>
  export default {
    name: 'ImageUpload',
    props: {
      fieldName: {
        type: String
      },
      campaignId: {
        type: Number
      },
      imageUrl: {
        type: String
      }
    },
    data () {
      return {
        uploadPercentage: 0,
        dragAndDropCapable: false,
        file: null,
        uploading: false,
        hasError: false
      }
    },
    methods: {
      determineDragAndDropCapable () {
        const div = document.createElement('div')
        return (('draggable' in div)
          || ('ondragstart' in div && 'ondrop' in div))
          && 'FormData' in window
          && 'FileReader' in window
      },
      removeFile (key) {
        this.files.splice(key, 1)
      },
      deleteImage () {
        let formData = new FormData()
        formData.append(this.fieldName, [])
        this.sendRequest(formData)
      },
      submitFile () {
        let formData = new FormData()

        formData.append(this.fieldName, this.file)
        this.sendRequest(formData)
      },
      sendRequest(data) {
        this.uploading = true
        this.axios.patch(`/api/v1/campaigns/${this.campaignId}/`,
          data,
          {
            headers: {
              'Content-Type': 'multipart/form-data'
            },
            onUploadProgress: progressEvent => {
              this.uploadPercentage = parseInt(Math.round((progressEvent.loaded * 100) / progressEvent.total))
            }
          }
        ).then(({data}) => {
          this.$emit('image-changed', this.fieldName, data[this.fieldName])
          this.uploading = false
        }).catch((error) => {
          console.log('FAILURE!!')
          console.log(error)
          this.uploading = false
        })
      },
      uploadFile (e) {
        this.file = e.target.files[0]
        this.submitFile()
      }
    },
    mounted () {

      const vm = this
      this.dragAndDropCapable = this.determineDragAndDropCapable()
      if (this.dragAndDropCapable) {
        ['drag', 'dragstart', 'dragend', 'dragover', 'dragenter', 'dragleave', 'drop'].forEach(evt => {
          vm.$refs.fileform.addEventListener(evt, e => {
            e.preventDefault()
            e.stopPropagation()
          })
        });

        ['dragover', 'dragenter'].forEach(evt => {
          vm.$refs.fileform.addEventListener(evt, e => {
            vm.$refs.fileform.classList.add('is-dragover')
          })
        });

        ['dragleave', 'dragend', 'drop'].forEach(evt => {
          vm.$refs.fileform.addEventListener(evt, e => {
            vm.$refs.fileform.classList.remove('is-dragover')
          })
        })

        vm.$refs.fileform.addEventListener('drop', function (e) {
          vm.file = e.dataTransfer.files[0]
          vm.submitFile()
        }.bind(this))

        vm.$refs.fileform.addEventListener('drop', function (e) {
          vm.file = e.dataTransfer.files[0]
          vm.submitFile()
        }.bind(this))
      }
    }
  }
</script>

<style lang="scss" scoped>
  .box__dragndrop,
  .box__uploading,
  .box__success,
  .box__error {
    display: none;
  }

  .box.has-advanced-upload {
    background-color: white;
    outline: 2px dashed black;
    outline-offset: -10px;
    height: 100px;
    position: relative;
    .box__dragndrop {
      display: inline;
    }
    input, .box__button {
      display: none
    }
    .box__input label {
      text-align: center;
      position: absolute;
      top: 0;
      right: 0;
      bottom: 0;
      left: 0;
      padding: 20px;
      cursor: pointer;
    }
  }

  .box.is-dragover {
    background-color: grey;
  }

  .box.is-uploading .box__input {
    display: none;
  }

  .box.is-uploading .box__uploading {
    display: block;
  }
  .preview {
    width: 300px;
    height: 300px;
  }
</style>
