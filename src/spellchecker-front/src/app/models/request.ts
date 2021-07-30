export class Request {
  request_id: string;
  request_date: any;
  request_text: string;
  request_response: string;
  constructor(request_id: string, request_date: any, request_text: string, request_response: string ){
    this.request_id = request_id;
    this.request_date = request_date;
    this.request_text = request_text;
    this.request_response = request_response;
  }
}
