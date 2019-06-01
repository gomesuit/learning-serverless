require 'json'

def hello(event:, context:)
  {
    statusCode: 200,
    body: JSON.pretty_generate(event)
  }
end
