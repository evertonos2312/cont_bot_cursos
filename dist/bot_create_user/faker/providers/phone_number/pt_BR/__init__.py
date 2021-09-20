from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        '+55 (011) #### ####',
        '+55 (021) #### ####',
        '+55 (031) #### ####',
        '+55 (041) #### ####',
        '+55 (051) #### ####',
        '+55 (061) #### ####',
        '+55 (071) #### ####',
        '+55 (081) #### ####',
        '+55 (084) #### ####',
        '+55 11 #### ####',
        '+55 21 #### ####',
        '+55 31 #### ####',
        '+55 41 #### ####',
        '+55 51 #### ####',
        '+55 61 #### ####',
        '+55 71 #### ####',
        '+55 81 #### ####',
        '+55 84 #### ####',
        '+55 (011) ####-####',
        '+55 (021) ####-####',
        '+55 (031) ####-####',
        '+55 (041) ####-####',
        '+55 (051) ####-####',
        '+55 (061) ####-####',
        '+55 (071) ####-####',
        '+55 (081) ####-####',
        '+55 (084) ####-####',
        '+55 11 ####-####',
        '+55 21 ####-####',
        '+55 31 ####-####',
        '+55 41 ####-####',
        '+55 51 #### ####',
        '+55 61 ####-####',
        '+55 71 ####-####',
        '+55 81 ####-####',
        '+55 84 ####-####',
        '(011) #### ####',
        '(021) #### ####',
        '(031) #### ####',
        '(041) #### ####',
        '(051) #### ####',
        '(061) #### ####',
        '(071) #### ####',
        '(081) #### ####',
        '(084) #### ####',
        '11 #### ####',
        '21 #### ####',
        '31 #### ####',
        '41 #### ####',
        '51 #### ####',
        '61 #### ####',
        '71 #### ####',
        '81 #### ####',
        '84 #### ####',
        '(011) ####-####',
        '(021) ####-####',
        '(031) ####-####',
        '(041) ####-####',
        '(051) ####-####',
        '(061) ####-####',
        '(071) ####-####',
        '(081) ####-####',
        '(084) ####-####',
        '11 ####-####',
        '21 ####-####',
        '31 ####-####',
        '41 ####-####',
        '51 #### ####',
        '61 ####-####',
        '71 ####-####',
        '81 ####-####',
        '84 ####-####',
        '0300 ### ####',
        '0500 ### ####',
        '0800 ### ####',
        '0900 ### ####',
        '0300-###-####',
        '0500-###-####',
        '0800-###-####',
        '0900-###-####',
    )

    msisdn_formats = (
        '55119########',
        '55219########',
        '55319########',
        '55419########',
        '55519########',
        '55619########',
        '55719########',
        '55819########',
        '55849########',
    )

    cellphone_formats = (
        '+55 ## 9#### ####',
        '+55 ## 9 #### ####',
        '+55 (0##) 9#### ####',
        '+55 (##) 9#### ####',
        '+55 (##) 9 #### ####',
        '+55 ## 9####-####',
        '+55 ## 9 ####-####',
        '+55 (0##) 9####-####',
        '+55 (##) 9####-####',
        '+55 (##) 9 ####-####',
    )

    services_phones_formats = (
        '100',
        '128',
        '151',
        '152',
        '153',
        '156',
        '180',
        '181',
        '185',
        '188',
        '190',
        '191',
        '192',
        '193',
        '194',
        '197',
        '198',
        '199',
    )

    def cellphone_number(self):
        pattern = self.random_element(self.cellphone_formats)
        return self.numerify(self.generator.parse(pattern))

    def service_phone_number(self):
        pattern = self.random_element(self.services_phones_formats)
        return self.numerify(self.generator.parse(pattern))