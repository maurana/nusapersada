import api from "@/utils/api"

class SalesService {
  getAll(data, page) {
    return api.post(`/sales?page=${page}`, JSON.stringify(data))
  }
}

export default new SalesService()