from flask import jsonify, request
from flask.views import MethodView
from webargs import fields
from webargs.flaskparser import HTTPException, parser

from src.controllers.words import ControllerWords
from src.exceptions import (AppError, ErrorBody, ErrorContentTypeInvalid,
                            ErrorOrderInvalid)


class ViewWordsDefault(MethodView):

    init_every_request = False

    @property
    def _controller_words(self):
        return ControllerWords()

    def _validate_content_type(self):
        if request.content_type != 'application/json':
            raise ErrorContentTypeInvalid("Content type Invalid {}".format(request.content_type))

    def _exect_fuction(self, func):
        try:
            return func()
        except HTTPException as error:
            return jsonify({"error": error.data["messages"]}), error.code
        except AppError as error:
            return jsonify({"error": str(error)}), error.status
        except Exception:
            return jsonify({"error": "internal server error"}), 500

    def _method_not_allowed(self):
        return jsonify({"errror": "Method Not Allowed"}), 405


class WordsCountVowels(ViewWordsDefault):
    __params = {
        "words": fields.List(fields.Str(required=True))
    }

    def __post(self):
        self._validate_content_type()
        params = parser.parse(self.__params)
        if not params:
            raise ErrorBody("Body invalid!")
        response = self._controller_words.wowels_count(params["words"])
        return jsonify(response)

    def post(self):
        return self._exect_fuction(self.__post)

    def get(self):
        return self._exect_fuction(self._method_not_allowed)

    def delete(self):
        return self._exect_fuction(self._method_not_allowed)

    def put(self):
        return self._exect_fuction(self._method_not_allowed)

    def patch(self):
        return self._exect_fuction(self._method_not_allowed)


class WordsSort(ViewWordsDefault):
    __params = {
        "words": fields.List(fields.Str(required=True)),
        "order": fields.Str(required=True)
    }

    def __post(self):
        self._validate_content_type()
        params = parser.parse(self.__params)
        order = params.get("order")
        if order not in ["asc", "desc"]:
            raise ErrorOrderInvalid("Param invalid to order. Params valids 'asc' or 'desc'.")

        response = self._controller_words.sort_list(params["words"], order)
        return jsonify(response)

    def post(self):
        return self._exect_fuction(self.__post)

    def get(self):
        return self._exect_fuction(self._method_not_allowed)

    def delete(self):
        return self._exect_fuction(self._method_not_allowed)

    def put(self):
        return self._exect_fuction(self._method_not_allowed)

    def patch(self):
        return self._exect_fuction(self._method_not_allowed)
