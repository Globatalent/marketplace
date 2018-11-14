export default function getCurrencySymbol (code) {
  switch (code) {
    case 'USD':
      return '$'
    case 'EUR':
      return '€'
    default:
      return code
  }
}
