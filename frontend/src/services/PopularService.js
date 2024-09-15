import api from "@/utils/api"

class PopularService {
  getAll(data) {
    return api.post(`/products_popular`, JSON.stringify(data))
  }
}

export default new PopularService()