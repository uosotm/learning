import moment from 'moment'

function dateToString (date) {
  if (date) {
    return moment(date).format('MMMM Do YYYY, h:mm:ss a')
  }
  return ''
}

function reverse (messages) {
  return messages.reverse()
}

export {
  dateToString,
  reverse
}
