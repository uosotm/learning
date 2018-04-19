<template>
  <div id="app" class="jumbotron">
    <div class="container">
      <h1>Hello! Nice to meet you!</h1>
      <hr />
      <form @submit="addMessage" class="mb-3">
        <div class="form-group">
          <input class="form-control"
                 v-model="newMessage.title"
                 maxlength="40"
                 autofocus
                 placeholder="Please introduce yourself :)" />
        </div>
        <div class="form-group">
          <textarea class="form-control"
                    v-model="newMessage.text"
                    placeholder="Leave your message!"
                    rows="3">
          </textarea>
        </div>
        <button class="btn btn-primary" type="submit">Send</button>
      </form>
      <div class="card-columns">
        <card class="border-success"
              :title="'Hello!'"
              :text="'This is our fixed card!'"
              :footer="'Added on ' + dateToString(Date.now())"></card>
        <card v-for="(message, index) in messages"
              :key="index"
              :title="message.title"
              :text="message.text"
              :footer="'Added on ' + dateToString(message.timestamp)"></card>
      </div>
    </div>
  </div>
</template>

<script>
import Card from './components/Card'
import Firebase from 'firebase'
import { dateToString } from './utils/utils'

let config = {
  apiKey: process.env.API_KEY,
  authDomain: process.env.AUTH_DOMAIN,
  databaseURL: process.env.DATABASE_URL,
  projectId: process.env.PROJECT_ID,
  storageBucket: process.env.STORAGE_BUCKET,
  messagingSenderId: process.env.MESSAGING_SENDER_ID
}
let app = Firebase.initializeApp(config)
let db = app.database()
let messagesRef = db.ref('messages')

export default {
  data () {
    return {
      newMessage: {
        title: '',
        text: '',
        timestamp: null
      }
    }
  },
  name: 'App',
  firebase: {
    messages: messagesRef
  },
  computed: {
    reversedMessages: function () {
      return this.messages.slice().reverse()
    }
  },
  methods: {
    dateToString: dateToString,
    addMessage (e) {
      e.preventDefault()
      if (this.newMessage.title === '') {
        return
      }
      this.newMessage.timestamp = Date.now()
      messagesRef.push(this.newMessage)
      this.newMessage.text = ''
      this.newMessage.title = ''
      this.newMessage.timestamp = null
    }
  },
  components: {
    Card
  }
}
</script>
