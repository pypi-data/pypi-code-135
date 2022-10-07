# from umvlib.umv import Umov
import datetime
import xml.etree.ElementTree as ET
from src.umvlib.umv import Umov
from src.umvlib.Fields import Fields as f
from src.umvlib.Constants import Constants as c
import csv, sys, os, shutil, time

umov = Umov('34763ee6c4d60e2fe3509e2329ebf1c05acf74')

COLETA = 'COLETA MATRIZ'
DEVOLUCAO = 'DEVOLUÇÃO MATRIZ'


def process_file(file_path):
    path = 'C:\\Users\\User\\Desktop\\aprovacao'
    # Approve
    with open(file_path, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)  # Skip headers
        for row in reader:
            if len(row) > 0:
                execution_id = row[0]
                umov.approve_activity_history(execution_id=execution_id)

    # Group
    with open(file_path, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        try:
            movement_type_index = next(reader).index('Tipo de Movimento')
        except ValueError:
            movement_type_index = None
            print(
                'ERRO: Nao foi possível identificar o tipo de movimentação. Coluna "Tipo de Movimento" não encontrada.')
            exit()
        map_filter_1_schedule = {}
        for row in reader:
            if len(row) > 0:
                execution_id = row[0]
                try:
                    print(f'Reading activity_history_hierarchical for {execution_id}')
                    activity_history_hierarchical = umov.get_activity_history_hierarchical(execution_id)
                    history = ET.fromstring(activity_history_hierarchical)
                    history_schedule = history.find(f.SCHEDULE)
                    sections_data = []
                    filter_1 = None
                    print(f'Capturing sections fields for {execution_id}')
                    for section in history.find(f.SECTIONS).findall(f.SECTION):
                        new_section = {
                            f.ALT_ID: section.find(f.ALT_ID).text,
                            f.ITEMS: [],
                        }
                        for item in section.find(f.ITEMS).findall(f.ITEM):
                            new_item = {
                                f.ID: item.find(f.ID).text,
                                f.FIELDS: [],
                            }
                            for field in item.find(f.FIELDS).findall(f.FIELD):
                                field_history = field.find(f.FIELD_HISTORY)
                                value = field_history.find(f.VALUE).text
                                value_for_exibition = field_history.find('valueForExibition').text
                                if row[movement_type_index] == COLETA:
                                    if field.find(f.ALT_ID).text == 'situacao_anterior':
                                        value = '06'
                                        value_for_exibition = f'{value} - Devolvido matriz'
                                    elif field.find(f.ALT_ID).text == 'situacao_atual':
                                        value = '02'
                                        value_for_exibition = f'{value} - Em trânsito para filial'
                                elif row[movement_type_index] == DEVOLUCAO:
                                    if field.find(f.ALT_ID).text == 'situacao_anterior':
                                        value = '05'
                                        value_for_exibition = f'{value} - Em trânsito para matriz'
                                    elif field.find(f.ALT_ID).text == 'situacao_atual':
                                        value = '06'
                                        value_for_exibition = f'{value} - Devolvido matriz'
                                else:
                                    print('ERRO: Tipo de movimentação desconhecido.')
                                    exit()
                                new_field = {
                                    f.ALT_ID: field.find(f.ALT_ID).text,
                                    f.FIELD_HISTORY: {
                                        f.VALUE: value,
                                        f.VALUE_FOR_EXHIBITION: value_for_exibition,
                                    }
                                }
                                # TODO: Check this
                                if new_field[f.ALT_ID] == 'grupo_cliente':
                                    filter_1 = new_field[f.FIELD_HISTORY][f.VALUE]
                                if new_field[f.ALT_ID]:
                                    new_item[f.FIELDS].append(new_field)
                            new_section[f.ITEMS].append(new_item)
                        sections_data.append(new_section)
                    print('Sections data', sections_data)
                    if filter_1 and filter_1 not in map_filter_1_schedule:
                        print(f'Creating schedule for group {filter_1}')
                        new_schedule_alt_id = umov.create_schedule(
                            update_if_exists=False,
                            service_local=history_schedule.find(f.SERVICE_LOCAL).find(f.ALT_ID).text,
                            agent='master',  # history_schedule.find(f.AGENT).find(f.ALT_ID).text,
                            activity_type=history.find(f.ACTIVITY).find(f.ALT_ID).text,
                            schedule_type=history_schedule.find(f.SCHEDULE_TYPE).find(f.ALT_ID).text,
                            filter_1=filter_1,
                        )
                        print(f'Created schedule {new_schedule_alt_id} for group {filter_1}')
                        map_filter_1_schedule[filter_1] = {
                            f.ALT_ID: new_schedule_alt_id,
                            f.SERVICE_LOCAL: history_schedule.find(f.SERVICE_LOCAL).find(f.ALT_ID).text,
                            f.SCHEDULE_TYPE: history_schedule.find(f.SCHEDULE_TYPE).find(f.ALT_ID).text,
                            f.AGENT: history_schedule.find(f.AGENT).find(f.ALT_ID).text,
                        }
                        print(f'Stored schedule info {map_filter_1_schedule[filter_1]}')
                    print(f'Creating activity history for schedule {map_filter_1_schedule[filter_1][f.ALT_ID]}')
                    umov.create_activity_history(
                        alternative_identifier=map_filter_1_schedule[filter_1][f.ALT_ID],
                        activity={'alternative_identifier': history.find(f.ACTIVITY).find(f.ALT_ID).text},
                        sections=sections_data,
                    )
                    print(f'Activity history created')
                except Exception as e:
                    print(e)

        print('Updating schedules')
        for schedule in map_filter_1_schedule.values():
            print(f'Updating {schedule[f.ALT_ID]} situation to {c.RETURNED_FROM_FIELD} (returned from field)')
            umov.create_schedule(
                update_if_exists=True,
                service_local=schedule[f.SERVICE_LOCAL],
                alternative_identifier=schedule[f.ALT_ID],
                situation=c.RETURNED_FROM_FIELD,
                schedule_type=schedule[f.SCHEDULE_TYPE],
            )


if __name__ == '__main__':
    path = os.getcwd()
    processed_files_path = os.path.join(path, "processed")
    if not os.path.exists(processed_files_path):
        os.makedirs(processed_files_path)
    try:
        for file in os.listdir(path):
            if file.endswith(".csv") or file.endswith(".CSV"):
                process_file(os.path.join(path, file))
                shutil.move(os.path.join(path, file),
                            os.path.join(processed_files_path, f'{str(datetime.datetime.now())}_{file}'))
        time.sleep(60)
    except KeyboardInterrupt as e:
        raise e
    except Exception as e:
        print(e)
        print("Error!", sys.exc_info()[0])
